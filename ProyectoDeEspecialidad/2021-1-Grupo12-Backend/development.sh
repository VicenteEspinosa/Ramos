#!/bin/bash

export MONGO_USER=user
export MONGO_PW=userpw

export COMPOSE_PROJECT_NAME=osam-backend

# Require sudo if user is not in docker group
if ! (id -nG "$USER" | grep -qw "docker" ;); then
    PREFIX="sudo -E"
fi

DOCKERCP_CMD="$PREFIX docker-compose -f docker-compose.dev.yml"
DOCKER_CMD="$PREFIX docker"

remove_containers() {
    eval "$DOCKERCP_CMD rm -v -f > /dev/null"
}

stop() {
    eval "$DOCKERCP_CMD stop"
}

drop_db() {
    stop
    remove_containers
    eval "$DOCKER_CMD volume rm -f osam-backend_mongodb_data"
    echo 'Database Dropped Succesfully!'
}

migrate_db() {
    echo "Migrating database!"
    eval "$DOCKERCP_CMD run django poetry run osam_backend/manage.py migrate"
}

seed_db() {
    echo 'Applying seeds to database!'
    eval "$DOCKERCP_CMD run django poetry run osam_backend/manage.py" \
         "loaddata osam_backend/backend_app/seed/*"
}

reset_db() {
    drop_db
    migrate_db
    seed_db
    echo "Database succesfully reset! Run ./development.sh and see it on" \
     "http://localhost:8081"
}

setup() {
    eval "$DOCKERCP_CMD build"
    migrate_db
    seed_db
    echo
    echo "Setup finished! Now simply run ./development.sh and start hacking!"
}

development() {
    remove_containers
    eval "$DOCKERCP_CMD up -d"
    eval "$DOCKERCP_CMD logs --tail=30 -f django"
    stop
}

uninstall() {
    eval "$DOCKERCP_CMD down --volumes"
}

fix_permissions() {
    echo 'Fixing permissions!'
    sudo chown -R "$USER:$USER" .
}

shell() {
    eval "$DOCKERCP_CMD run django bash"
    fix_permissions
}

finish() {
    echo "Handling signal interrupt"
}


trap finish INT

opt="$1"

case "$opt" in 

    setup)
        setup
        ;;
    db:migrate)
        migrate_db
        ;;
    db:drop)
        drop_db
        ;;

    db:reset)
        reset_db
        ;;

    shell)
        shell
        ;;

    uninstall)
        uninstall
        ;;
    *)
        echo "No option provided, starting development mode!"
        development
        ;;
esac