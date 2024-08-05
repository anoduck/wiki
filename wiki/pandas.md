```text
#  ____        ____                 _
# |  _ \ _   _|  _ \ __ _ _ __   __| | __ _ ___
# | |_) | | | | |_) / _` | '_ \ / _` |/ _` / __|
# |  __/| |_| |  __/ (_| | | | | (_| | (_| \__ \
# |_|    \__, |_|   \__,_|_| |_|\__,_|\__,_|___/
#        |___/
#
```

## Working with Pandas is a gigantic pain in the ass!

Make no mistake about it, python pandas is a brilliant feat of programming genius. The pandas library provides
a robust datastructure that allows processing massive amounts of data efficiently and with great speed. The
Pandas library also allows programmers to convert massive amounts of data into nearly every datastructure
available. It can read directly from csv files, json files, databases, and whatever other type of data storage
you can thing of. It is without a doubt a zenith of modern pythonistic engineering.

Unfortunately, due to it's abstract and robust nature, it's a tremendous pain in the ass to work with. There
are simply too many methods and required parameters to keep up with unless you work with it on a daily basis.
The Pandas library also has it's own way of doing things, which may or may not jive with how you do things.
Then there are a number of informal "hacks" not mentioned in the docs, on how to get common tasks
accomplished. It is brilliant, yes, but so was the first land mine.

### Cheat Sheet

1. Create Dataframe: `dataframe = pd.DataFrame(record, columns = ['$COLUMN_NAMES'])`
2. Select Row by Condition: `$DATAFRAME_NAME[$DATAFRAME_NAME['$COLUMN_NAME'] == $VALUE]` or `$DATAFRAME_NAME.loc[$DATAFRAME_NAME['$COLUMN_NAME'] == $VALUE]`
3. Test for equality: `$DATAFRAME_NAME.$PROPERTY.equals($TEST_VALUE)`
4. Add column headers to pre-existing dataframe: `$DATAFRAME_NAME.columns = ['$COLUMN_NAMES']`
5. Find the most common occurring value in a column: 
    ```python
    df = pd.DataFrame({'care': 98, 'robert': 43, 'shit': 100}, columns=['word', 'score'])
    grouped = df.groupby('word')
    word_rep = grouped['word'].agg(lambda x: x.mode().iloc[0])
    ```
6. find the maximum value of a column: `df.loc[df['score'].idxmax()]`
7. Get first item from series: '<$Series>.item()'
8. Create series from dataframe: `df.<$COLUMN_LABEL>` or `df['<$COLUMN_LABEL>']`

