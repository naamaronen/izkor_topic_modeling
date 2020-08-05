import altair as alt
import pandas as pd
import xlrd

wb = xlrd.open_workbook("tutorial_composition.xlsx")
sheet = wb.sheet_by_index(0)

num_of_topics = 20
data = []
for i in range(21430):
    year = sheet.cell_value(i, 1).split('/')[6].split('_')[0]
    gender = sheet.cell_value(i, 1).split('/')[6].split('_')[1]
    if gender == "f":
        gender = 2
    else:
        gender = 1
    for j in range(num_of_topics):
        x = {"topic": j, "year": int(year), "rate": sheet.cell_value(i,j+2), "sex": gender}
        data.append(x)

data_frame = pd.DataFrame(data)

alt.Chart(data_frame).mark_area().encode(
    alt.X('year:O',
        scale=alt.Scale(zero=False)
    ),
    alt.Y('sum(rate):Q', stack='center', axis=None),
    alt.Color('topic:N',
        scale=alt.Scale(scheme='category20b'))
).properties(
    width=800,
    height=300
).save('chart.html')



pink_blue = alt.Scale(domain=('Male', 'Female'),
                      range=["steelblue", "salmon"])

slider = alt.binding_range(min=1900, max=2020, step=10)
select_year = alt.selection_single(name="choose a", fields=['year'],
                                   bind=slider, init={'year': 2000})

alt.Chart(data_frame).mark_bar().encode(
    x=alt.X('sex:N', title=None),
    y=alt.Y('rate:Q'),
    color=alt.Color('sex:N', scale=pink_blue),
    column='topic:O'
).properties(
    width=20
).add_selection(
    select_year
).transform_calculate(
    "sex", alt.expr.if_(alt.datum.sex == 1, "Male", "Female")
).transform_filter(
    select_year
).configure_facet(
    spacing=8
).save('chart1.html')