import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Reducer;

import java.io.IOException;

public class red extends Reducer<NullWritable, Text,NullWritable,Text> {

    @Override
    protected void reduce(NullWritable key, Iterable<Text> values, Reducer<NullWritable, Text, NullWritable, Text>.Context context) throws IOException, InterruptedException {

        // for循环遍历结果数组
        for (Text text : values) {
            // 正则匹配'|'分割文本, 职位名称|公司名称|所在城市|发布日期|薪资
            String[] dataList = text.toString().split("\\|");
            // 判断数组长度是否为5
            if (dataList.length == 5) {
                // 使用| 连接数组字符串，并输出最终数据
                context.write(NullWritable.get(), new Text(String.join("|", dataList)));
            }
        }
    }
}