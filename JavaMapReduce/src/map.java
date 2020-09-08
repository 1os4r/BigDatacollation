import java.io.IOException;
import java.util.ArrayList;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class map extends Mapper<LongWritable,Text, NullWritable,Text> {

    @Override
    protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, NullWritable, Text>.Context context) throws IOException, InterruptedException {
        // 使用匹配的逗号分割一行文本
        String[] strList = value.toString().split(",");
        // 声明ArrayList数组用于存放数据
        ArrayList<String> arrayList = new ArrayList<String>();
        // for循环遍历数据
        for (int i = 0; i < strList.length; i++) {
            String str = strList[i].trim();
            // 判断并过滤空数据
            if (str.isEmpty() || str.equals("[]") || str.equals("[\"\"]")) {
                return;
            }
            arrayList.add(strList[i]);
        }
        // 将逗号分隔转为使用`|`分隔
        context.write(NullWritable.get(), new Text(String.join("|", arrayList)));

    }

}


