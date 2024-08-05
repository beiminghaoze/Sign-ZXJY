import sys
import pushinfo
from process import *


def main(users):
    if config['log_report']:
        logData = ""

    for user in users:
        print(f"=========={user['name']}==========")
        waittime = random_Time(config['range_time'])
        print(f"本次随机 {waittime} s")
        time.sleep(float(waittime))
        logging.info(f"{user['name']} 随机 {waittime} s")
        now_localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        TDOA = datetime.datetime.strptime(user['enddate'], '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(
            now_localtime, '%Y-%m-%d %H:%M:%S')
        info = login_and_sign_in(user=user, endday=TDOA.days)
        logging.info(f"{user['name']} 的返回值为{info}")
        if config['log_report']:
            try:
                for i in range(0, len(info)):
                    logData = logData + info[i].replace("\n", "").replace("未在", "。未在").replace("剩余", "。剩余")
                logData = logData + "\n"
            except:
                pass

        for i in range(0, len(info)):
            print(f"{info[i]}")

    if config['log_report']:
        logging.info(
            pushinfo.Send_Email(config['log_report_data']['emailUsername'],
                                config['log_report_data']['emailPassword'],
                                config['log_report_data']['emailAddress'],
                                config['log_report_data']['emailPort'],
                                config['log_report_data']['Receiver'], "职校家园打卡简要日志",
                                logData))


if __name__ == "__main__":
    print("\033[32m====================进程开始====================\033[0m")
    main(load_users_from_json("all-users.json"))
    print("\033[32m====================进程结束====================\033[0m")
    print("5 s后自动退出！")
    time.sleep(5)
