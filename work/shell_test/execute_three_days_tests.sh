#!/bin/bash
declare -A jp=(
    ['pre_begin']='テストの準備を開始します。'
    ['pre_failed']='テストの準備に失敗しました。'
    ['pre_succeeded']='テストの準備が正常に完了しました。'
    ['before_exec_msg1']='このテストは有効期限が3日のシークレットURLのテストのため、Dockerの時間を4日ずらす必要があります。'
    ['before_exec_msg2']='そのため、以下のコマンドをWEKOシステムのあるマシンで実行してください。'
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
    ['before_exec_msg1']='This test is for a secret URL with a 3-day expiration date, so you need to shift the time in Docker by 4 days.'
    ['before_exec_msg2']='Therefore, run the following command on the machine where the WEKO system is located.'
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
pytest shell_test/test_secret_url_three_days.py::TestPreparation

# check for successful completion
if [ $? -ne 0 ]; then
    echo ${lang['pre_failed']}
    find secret_url -type f | grep -v -E 'example.txt' | xargs rm -f
    exit 1
fi
echo ${lang['pre_succeeded']}

# wait for date operation
echo ${lang['before_exec_msg1']}
echo ${lang['before_exec_msg2']}
echo "date -s \"4 days\""
sleep 5

# confirm that the command execution is complete
echo ${lang['confirm_exec']}
ConfirmExecution

# execute the test
pytest shell_test/test_secret_url_three_days.py::TestExecution

# check for successful completion
if [ $? -ne 0 ]; then
    echo ${lang['exec_failed']}
    echo ${lang['after_exec_msg']}
    echo "date -s \"4 days ago\""
    find secret_url -type f | grep -v -E 'example.txt' | xargs rm -f
    exit 1
fi

# restore the date
echo ${lang['exec_succeeded']}
echo ${lang['after_exec_msg']}
echo "date -s \"4 days ago\""
exit 0
