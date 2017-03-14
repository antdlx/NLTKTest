#-*- coding:utf-8 -*-
import main
import BigHead2
import Affix2
import subprocess
import OutputFormat
class ClassMain2:
    def doMain2(self):

        mmain = main.ClassMain()
        mmain.doMain()

        big = BigHead2.ClassBigHead2()
        big.doBigHead2()

        aff = Affix2.ClassAffix2()
        aff.doAffix2()

        # subprocess.Popen("del output_result.txt",shell=True)
        # subprocess.Popen("crf_test.exe -m model118x outputAffix.txt >> output_result.txt",shell=True)
        #注意：Popen是并行的，不会阻塞父进程，call是阻塞式的，父进程会等待子进程完成任务才继续
        subprocess.call("del output_result.txt",shell=True)
        subprocess.call("crf_test.exe -m model118x outputAffix.txt >> output_result.txt",shell=True)

        #format
        oformat = OutputFormat.ClassOutputFormat()
        result = oformat.doFormat()
        return result

