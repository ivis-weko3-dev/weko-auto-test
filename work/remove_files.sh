# screenshotsフォルダ内のexample.txtを除くすべてのファイルを削除
find /work/screenshots -type f | grep -v -E 'example.txt' | xargs rm -rf

# downloadsフォルダ内のexample.txtを除くすべてのファイルを削除
target=('application_for_use' 'secret_url')
for t in ${target[@]}; do
    find /work/downloads/$t -type d | grep -v -x -E '/work/downloads/'$t | xargs rm -rf
done

# mailフォルダ内にある各ユーザごとのフォルダ内の
# newフォルダ内のexample.txtを除くすべてのファイルを削除
find /work/mail/*/new -type f | grep -v -E 'example.txt' | xargs rm -rf