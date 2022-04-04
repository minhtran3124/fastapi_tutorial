export LOCAL_VENV="fastapi_tutorial_env"


function init_env() {
    echo "===> Creating virtualenv $LOCAL_VENV ..."
    python3 -m venv $LOCAL_VENV
}

function activate_env() {
    echo -e "\n"
    echo "===> Loading virtualenv $LOCAL_VENV ..."
    source $LOCAL_VENV/bin/activate
}

function install_required_tools() {
    echo -e "\n"
    echo "===> Installing required tools ..."
    pip install pip-tools
}

function complie_requirements() {
    echo -e "\n"
    echo "===> Compling requirements ..."
    pip-compile requirements.in
}

function install_packages() {
    echo -e "\n"
    echo "===> Installing requirements ..."
    pip install -r requirements.txt
}

function run_setup() {
    echo -e "\n"
    echo "===> Running setup ..."

    init_env
    activate_env
    install_required_tools
    complie_requirements
    install_packages
}

function run_app() {
    echo -e "\n"
    echo "===> Running app ..."
    python src/main.py
}

function print_helper() {
    echo "==========================================================================
    run_setup:
        Create, activate env, install required tools and install packages

    run_app:
        Run application

    activate_env:
        Activate environment
=========================================================================="
}

print_helper
