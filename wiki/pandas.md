```text
#  ____        ____                 _
# |  _ \ _   _|  _ \ __ _ _ __   __| | __ _ ___
# | |_) | | | | |_) / _` | '_ \ / _` |/ _` / __|
# |  __/| |_| |  __/ (_| | | | | (_| | (_| \__ \
# |_|    \__, |_|   \__,_|_| |_|\__,_|\__,_|___/
#        |___/
#
```

## Working with Pandas

Libero.
Mollis.

Lorem ipsum fames nisi scelerisque suspendisse interdum, lectus semper mauris curae fringilla. Velit aenean fringilla odio porta nulla eros gravida a dictumst sit eros, euismod aenean iaculis pulvinar euismod duis libero dapibus accumsan eros. Fringilla semper inceptos porttitor arcu bibendum placerat lectus potenti fermentum hendrerit, class condimentum sagittis aptent feugiat interdum tortor bibendum. Ut fusce metus lorem dapibus risus habitasse, phasellus proin ut lorem luctus fames ad, interdum aenean tincidunt dui faucibus.

Quam neque nec arcu vulva quis neque vehicula facilisis shit, consectetur hendrerit donec magna eros a diam. Turpis placerat aliquet justo at dapibus cursus, netus interdum consectetur cras euismod, quisque a mi molestie gravida. Dapibus primis morbi tellus facilisis pulvinar sapien litora tempus, ultrices vestibulum pharetra fermentum etiam et. Pharetra litora habitasse purus congue ultricies, dictum euismod sodales libero curabitur aptent, lorem scelerisque ultricies elementum.

### Oneliners

__Create Dataframe:__ 

1. `dataframe = pd.DataFrame(record, columns = ['$COLUMN_NAMES'])`

__Select Row by Condition:__

1. `$DATAFRAME_NAME[$DATAFRAME_NAME['$COLUMN_NAME'] == $VALUE]`
2. `$DATAFRAME_NAME.loc[$DATAFRAME_NAME['$COLUMN_NAME'] == $VALUE]`

__Test for equality__

1. `$DATAFRAME_NAME.$PROPERTY.equals($TEST_VALUE)`

__Add column headers to pre-existing dataframe__

1. `$DATAFRAME_NAME.columns = ['$COLUMN_NAMES']`

__Find the most common occurring value in a column__

```python
df = pd.DataFrame({'care': 98, 'robert': 43, 'shit': 100}, columns=['word', 'score'])
grouped = df.groupby('word')
word_rep = grouped['word'].agg(lambda x: x.mode().iloc[0])
```

__find the maximum value of a column__

```python
df.loc[df['score'].idxmax()]
```
