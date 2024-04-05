sudo pkg install bash
Додайте bash до списку допустимих оболонок в файлі /etc/shells:
sudo sh -c 'echo "/usr/local/bin/bash" >> /etc/shells'
Змініть оболонку користувача на bash за допомогою команди chsh. Наприклад, для користувача з іменем "user":
chsh -s /usr/local/bin/bash root



echo $SHELL
echo $0

nano ~/.bashrc

---* 
Bash має вбудовану підтримку 256 кольорів, і налаштувати її дуже просто.

Встановіть пакет bash-completion:
sudo pkg install bash-completion
Додайте наступні рядки в свій файл ~/.bashrc:

Enable 256-color support for terminal
export TERM=xterm-256color

# Define 256-color variables
for i in {0..255}; do
    printf "\x1b[38;5;${i}mcolour${i} "
done
printf "\n"

Застосуйте зміни до поточного сеансу Bash, виконавши команду:
source ~/.bashrc

Щоб перевірити, чи налаштування працює, виконайте команду:
echo $TERM

Це повідомлення інформує вас про те, що ви можете включити бібліотеку автодоповнення для Bash. Для цього потрібно додати наступний код до вашого файлу .bashrc:
[[ $PS1 && -f /usr/local/share/bash-completion/bash_completion.sh ]] && \
        source /usr/local/share/bash-completion/bash_completion.sh



# Enable colored output for ls, grep, etc.
alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias fgrep='fgrep --color=auto'
alias egrep='egrep --color=auto'

# Enable colored output for directories in the output of ls
LS_COLORS='di=1;34:ln=1;35:so=1;32:pi=1;33:ex=1;31:bd=1;34:cd=1;34:su=0;41:sg=0;46:tw=1;34:ow=1;34'
export LS_COLORS

# Enable 256-color support for terminal
export TERM=xterm-256color

# Define 256-color variables
for i in {0..255}; do
    printf "\x1b[38;5;${i}mcolour${i} "
done
printf "\n"



---* conf
pkg install curl
curl https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash -o ~/.bashrc
