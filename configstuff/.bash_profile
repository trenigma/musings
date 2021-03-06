#aliases
alias ls='ls -GFh'
alias l="ls -al"
alias lp="ls -p"
alias h=history

#make cool colors in terminal
export PS1="\[\033[36m\]\u\[\033[m\]@\[\033[32m\]\h:\[\033[33;1m\]\w\[\033[m\]\$ "
export CLICOLOR=1
export LSCOLORS=ExFxBxDxCxegedabagacad

# general path munging
PATH=${PATH}:~/bin
PATH=${PATH}:/usr/local/bin

#unicode path stuff
export PATH=/usr/local/opt/icu4c/bin:$PATH
export PATH=/usr/local/opt/icu4c/sbin:$PATH

#python path stuff
export PATH=/usr/bin/python:$PATH

#java stuff
export JAVA_HOME=/usr/libexec/java_home

#maven stuff
export MAVEN_HOME=/Users/Tree/buildtools/apache-maven-3.5.2/bin:$PATH
