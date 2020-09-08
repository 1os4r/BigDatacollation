# Hadoop MapReduce启动脚本

```bash
HADOOP_CMD="hadoop"
STREAM_JAR_PATH="/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar"
INPUT_FILE_PATH="/input/data.txt"
OUTPUT_PATH="/result/test"
$HADOOP_CMD fs -rm -r  $OUTPUT_PATH
$HADOOP_CMD jar $STREAM_JAR_PATH \
        -input $INPUT_FILE_PATH \
        -output $OUTPUT_PATH \
        -mapper "python map.py" \
        -reducer "python reduce.py" \
        -file ./map.py \
        -file ./reduce.py
```



