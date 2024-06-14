# copy recipient_access file to /etc/postfix/
\cp ./recipient_access /etc/postfix/

# create or update recipient_access.db
postmap /etc/postfix/recipient_access

# restart postfix
systemctl restart postfix

# create user
cat ./recipient_access | while read line
do
    if [[ "$line" == *"@weko-selenium.jp"* ]]; then
        ARR=(${line//@/ })
        id ${ARR[0]}
        if [ $? -ne 0 ]; then
            useradd ${ARR[0]} -s /sbin/nologin
        fi
    fi
done
