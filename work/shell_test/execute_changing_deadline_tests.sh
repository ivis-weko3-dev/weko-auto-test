#!/bin/bash
declare -A jp=(
    ['pre_begin']='テストの準備を開始します。'
    ['pre_failed']='テストの準備に失敗しました。'
    ['pre_succeeded']='テストの準備が正常に完了しました。'
    ['change_begin']='有効期限の変更を開始します。'
    ['change_failed']='有効期限の変更に失敗しました。'
    ['change_succeeded']='有効期限の変更が正常に完了しました。'
    ['before_exec_msg1']='このテストは有効期限を3日から5日に変更するシークレットURLのテストです。'
    ['before_exec_msg2']='有効期限の変更後、3日を過ぎていても問題ないことを確認するため、Dockerの時間を4日ずらす必要があります。'
    ['before_exec_msg3']='そのため、以下のコマンドをWEKOシステムのあるマシンで実行してください。'
    ['confirm_exec']='コマンドの実行は完了しましたか？(y/n)'
    ['y_or_n']='yかnを入力してください。'
    ['exec_begin']='テストの実行を開始します。'
    ['confirm_interrupt']='テストの実行を中止しますか？(y/n)'
    ['exec_interrupt']='テストの実行を中止しました。'
    ['exec_failed']='テストの実行に失敗しました。'
    ['after_exec_msg']='マシンの時刻を戻すため、マシンの再起動または以下のコマンドを実行してください。'
    ['exec_succeeded']='テストの実行が正常に完了しました。'
)

declare -A en=(
    ['pre_begin']='Test preparation begins.'
    ['pre_failed']='Test preparation failed.'
    ['pre_succeeded']='Test preparation completed successfully.'
    ['change_begin']='Changing expiration date begins.'
    ['change_failed']='Changing expiration date failed.'
    ['change_succeeded']='Changing expiration date completed successfully.'
    ['before_exec_msg1']='This test is for a secret URL that changes the expiration date from 3 days to 5 days.'
    ['before_exec_msg2']='After changing the expiration date, you need to shift the time in Docker by 4 days to confirm that it is not a problem even after 3 days have passed.'
    ['before_exec_msg3']='Therefore, run the following command on the machine where the WEKO system is located.'
    ['confirm_exec']='Did you complete the command execution? (y/n)'
    ['y_or_n']='Please enter y or n.'
    ['exec_begin']='Test execution begins.'
    ['confirm_interrupt']='Do you want to interrupt the test execution? (y/n)'
    ['exec_interrupt']='Test execution interrupted.'
    ['exec_failed']='Test execution failed.'
    ['after_exec_msg']='To revert the machine time, restart the machine or run the following command.'
    ['exec_succeeded']='Test execution completed successfully.'
)

declare -A lang

function ConfirmLanguage() {
    read answer
    if [ -z $answer ]; then
        echo "jpかenを入力してください。/Please enter jp or en."
        ConfirmLanguage
    elif [ $answer = "jp" ]; then
        for i in ${!jp[@]}; do
            lang[$i]=${jp[$i]}
        done
    elif [ $answer = "en" ]; then
        for i in ${!en[@]}; do
            lang[$i]=${en[$i]}
        done
    else
        echo "jpかenを入力してください。/Please enter jp or en."
        ConfirmLanguage
    fi
}

function ConfirmExecution() {
    read answer
    if [ -z $answer ]; then
        echo ${lang['y_or_n']}
        ConfirmExecution
    elif [ $answer = "y" ]; then
        echo ${lang['exec_begin']}
    elif [ $answer = "n" ]; then
        echo ${lang['confirm_interrupt']}
        ConfirmInterruption
    else
        echo ${lang['y_or_n']}
        ConfirmExecution
    fi
}

function ConfirmInterruption() {
    read answer
    if [ -z $answer ]; then
        echo ${lang['y_or_n']}
        ConfirmInterruption
    elif [ $answer = "y" ]; then
        echo ${lang['exec_interrupt']}
        find secret_url -type f | grep -v -E 'example.txt' | xargs rm -f
        exit 0
    elif [ $answer = "n" ]; then
        echo ${lang['confirm_exec']}
        ConfirmExecution
    else
        echo ${lang['y_or_n']}
        ConfirmInterruption
    fi
}

# choose language
echo '言語を選択してください。/Please select a language.(jp/en)'
ConfirmLanguage

# execute the test prepalation process
echo ${lang['pre_begin']}
pytest shell_test/test_secret_url_changing_deadline.py::TestPreparation

# check for successful completion
if [ $? -ne 0 ]; then
    echo ${lang['pre_failed']}
    find secret_url -type f | grep -v -E 'example.txt' | xargs rm -f
    exit 1
fi
echo ${lang['pre_succeeded']}

# change expiration date
echo ${lang['change_begin']}
pytest shell_test/test_secret_url_changing_deadline.py::test_change_expiration_date

# check for successful completion
if [ $? -ne 0 ]; then
    echo ${lang['change_failed']}
    find secret_url -type f | grep -v -E 'example.txt' | xargs rm -f
    exit 1
fi
echo ${lang['change_succeeded']}

# wait for date operation
echo ${lang['before_exec_msg1']}
echo ${lang['before_exec_msg2']}
echo ${lang['before_exec_msg3']}
echo "date -s \"4 days\""
sleep 5

# confirm that the command execution is complete
echo ${lang['confirm_exec']}
ConfirmExecution

# execute the test
pytest shell_test/test_secret_url_changing_deadline.py::TestExecution

# check for successful completion
if [ $? -ne 0 ]; then
    echo ${lang['exec_failed']}
    echo ${lang['after_exec_msg']}
    echo "date -s \"4 days ago\""
    find secret_url -type f | grep -v -E 'example.txt' | xargs rm -f
    exit 1
fi

# reset the date
echo ${lang['exec_succeeded']}
echo ${lang['after_exec_msg']}
echo "date -s \"4 days ago\""
exit 0
