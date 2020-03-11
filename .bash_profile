function desktop {
  cd /Users/$USER/Desktop/$@
}

function parse_git_branch {
    git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}

# This function builds your prompt. It is called below
function prompt {
    # Define the prompt character
    local   CHAR="🤔 "

    # Define some local colors
    local   RED="\[\e[0;31m\]"
    local   BLUE="\[\e[0;34m\]"
    local   GREEN="\[\e[0;32m\]"
    local   GRAY_TEXT_BLUE_BACKGROUND="\[\e[37;44;1m\]"

    # Define a variable to reset the text color
    local   RESET="\[\e[0m\]"

    # ♥ ☆ - Keeping some cool ASCII Characters for reference

    # Here is where we actually export the PS1 Variable which stores the text for your prompt
    export PS1="\[\e]2;\u@\h\a[$GRAY_TEXT_BLUE_BACKGROUND\t$RESET]$RED\$(parse_git_branch) $GREEN\W\n$BLUE//$RED $CHAR $RESET"
      PS2='> '
      PS4='+ '
}

# Finally call the function and our prompt is all pretty
prompt

# Change color of directories for differentiation
# =====================
export CLICOLOR=1
export LSCOLORS=Exxxxxxxxxxxxxxxxxxxxx


# Aliases
# =====================
alias root='cd ~/bcroot'
alias l='ls -lah'
alias c='clear'
alias gp='git pull'
alias gitco='git checkout'
alias gadd='git add'
alias gits='git status'
alias gcm='git commit -m'
alias gcnvm='git commit --no-verify -m'
alias gbg='git branch | grep'
alias gpoh='git push origin head'
alias gclone='git clone git@github.com:TriggerMail/'
# testfeed csv_with_data partner_feed_file --rows ###
alias testfeed='~/bcroot/trigger_mail/src/venv/bin/python ~/bcroot/trigger_mail/src/chrono_feed_yaml_preview.py'
# testderprop derived_properties_file_path -p JSON_object (ex:'{"category": "Just untab all of those"}')
alias testderprop='PYTHONPATH=. ~/bcroot/trigger_mail/src/venv/bin/python ~/bcroot/trigger_mail/src/engine/yumli/dialects/validate_derived_properties.py -i '
alias addssh='ssh-add -K ~/.ssh/id_rsa'
addssh # automatically reregister github ssh key
alias gbdel='git branch -D '

alias bluecore_activate='eval `~/bcroot/devenv/bluecore activate`'
bluecore_activate
alias setup='python service_setup.py '

alias backserv='cd ~/bcroot/triggermail/cstools; python -m cstools.handlers open http://localhost:5000/'
alias frontserv='yarn run watch:cstools'

alias install_dep='python service_setup.py ~/bcroot/trigger_mail/src; pip install -r ~/bcroot/trigger_mail/src/requirements.txt --find-links=~/bcroot/trigger_mail/bluecore-built-packages'
alias remote='~/bcroot/trigger_mail/src/venv/bin/python ~/bcroot/trigger_mail/src/gae_console.py triggeredmail'

alias pup='node ~/bcroot/integrations/tools/pup_tiego/pup_tiego.js'
alias watch='bluecore_activate; node ~/bcroot/integrations/tools/node_watch.js'
alias jupyter_di="PYTHONPATH=~/bcroot/trigger_mail/src:~/bcroot/trigger_mail/src/service_lib/installed:~/bcroot/trigger_mail/data_insights ~/bcroot/trigger_mail/src/venv/bin/jupyter notebook"

alias findport="lsof -i"
alias killport="kill -9"
alias countrows="wc -l"

function frameworkpython {
 if [[ ! -z "$VIRTUAL_ENV" ]]; then
 PYTHONHOME=$VIRTUAL_ENV /usr/local/bin/python "$@"
 else
 /usr/local/bin/python "$@"
 fi
}

export PATH="$HOME/.yarn/bin:$HOME/.config/yarn/global/node_modules/.bin:$PATH"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
