import datetime


class screen_record():
    """
    adb adb对象
    save_path 录屏保存的路径
    delete_shot 录屏完成是否需要删除手机上的视频
    """

    def screen_record(self, adb, device, save_path, delete_record):
        file_name = self.get_file_name()
        screen_cap = adb.run("-s " + device + " shell screenrecord --time-limit 10 /sdcard/" + file_name)
        if self.check_result(screen_cap):
            # 录屏失败
            print('录屏失败：' + screen_cap)
            return
        pull = adb.run("-s " + device + " pull /sdcard/" + file_name + " " + save_path)
        if self.check_result(pull):
            # 拷贝出错了
            print('拷贝录屏失败：' + pull)
            return
        print("录屏成功，文件已保存至：" + save_path + file_name)
        # 删除
        if delete_record:
            adb.run("shell rm /sdcard/" + file_name)
        pass

    def get_file_name(self):
        return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + '.mp4'

    # 分析返回结果
    def check_result(self, result):
        if result.startswith('adb: error'):
            return True
