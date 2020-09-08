
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class Main {
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();
        // 1.创建一个job和任务入口
        Job job = Job.getInstance(configuration);
        job.setJarByClass(Main.class); // 设置main方法所在的class

        // 2.指定job的mapper和输出的类型<k2 v2>
        job.setMapperClass(map.class);// 指定Mapper类
        job.setMapOutputKeyClass(NullWritable.class); // k2的类型为空
        job.setMapOutputValueClass(Text.class); // v2的类型

        // 3.指定job的reducer和输出的类型<k4 v4>
        job.setReducerClass(red.class);// 指定Reducer类
        job.setOutputKeyClass(NullWritable.class); // k4的类型为空
        job.setOutputValueClass(Text.class); // v4的类型

        // 4.指定job的输入路径和输出路径
        FileInputFormat.setInputPaths(job, new Path("hdfs://localhost:9000/input/data.txt")); // 指定输入的数据文档
        FileOutputFormat.setOutputPath(job, new Path("hdfs://localhost:9000/output/zhilian/")); // 指定输出文件位置
        new Path("hdfs://localhost:9000/").getFileSystem(configuration).delete(new Path("hdfs://localhost:9000/output/zhilian/")); // 若存在则删除之前存在的目录
        // 5.执行job
        job.waitForCompletion(true);
        System.out.print(job.waitForCompletion(true) ? '0' : '1');

    }
}
