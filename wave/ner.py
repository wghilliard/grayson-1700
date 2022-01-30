import os

import httpx
from h2o_wave import Q, ui, app, main

NER_HOST = os.getenv("NER_HOST", "localhost:8080")

sample_markdown = """
# type some stuff below

e.g. _Apple is looking at buying U.K. startup for $1 billion_

"""

columns = [
    ui.table_column(
        name="text", label="Text", sortable=True, searchable=True, max_width="300"
    ),
    ui.table_column(name="type", label="Type", filterable=True),
]


@app("/ner")
async def serve(q: Q):
    input_text = q.args.input_text

    q.page["intro"] = ui.form_card(
        box="1 1 5 6",
        items=[
            ui.text(sample_markdown),
            ui.textbox(
                name="input_text",
                value=input_text if input_text else "",
                multiline=True,
            ),
            ui.buttons([ui.button(name="submit", label="Send It", primary=True)]),
        ],
    )
    await q.page.save()

    if q.args.submit:
        q.user.input_text = input_text

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(
                f"http://{NER_HOST}/ner", json={"text": input_text}
            )

        html = response.json()["html"]
        q.page["table_result"] = ui.form_card(
            box="6 1 6 6",
            items=[
                ui.table(
                    name="entities",
                    columns=columns,
                    rows=[
                        ui.table_row(
                            name=str(entity["id"]),
                            cells=[entity["text"], entity["label"]],
                        )
                        for entity in response.json()["entities"]
                    ],
                    groupable=True,
                    downloadable=True,
                    resettable=True,
                )
            ],
            title="Found Entities",
        )
        q.page["pretty_result"] = ui.frame_card(
            box="1 7 10 12", title="Pretty Text", content=html
        )

    await q.page.save()
