# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2020_06_28_001252) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "cita", force: :cascade do |t|
    t.date "date"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "user_id"
    t.bigint "restaurant_id"
    t.boolean "is_finished", default: false
    t.boolean "is_checked", default: false
    t.integer "user_2_id"
    t.boolean "is_reviewed"
    t.index ["restaurant_id"], name: "index_cita_on_restaurant_id"
    t.index ["user_id"], name: "index_cita_on_user_id"
  end

  create_table "cities", force: :cascade do |t|
    t.string "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "comments", force: :cascade do |t|
    t.text "content"
    t.integer "rating"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "user_id"
    t.bigint "restaurant_id"
    t.index ["restaurant_id"], name: "index_comments_on_restaurant_id"
    t.index ["user_id"], name: "index_comments_on_user_id"
  end

  create_table "gustos", force: :cascade do |t|
    t.string "nombre"
    t.string "descripcion"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "gustos_users", id: false, force: :cascade do |t|
    t.bigint "gusto_id", null: false
    t.bigint "user_id", null: false
    t.index ["gusto_id"], name: "index_gustos_users_on_gusto_id"
    t.index ["user_id"], name: "index_gustos_users_on_user_id"
  end

  create_table "matches", force: :cascade do |t|
    t.bigint "user_id"
    t.integer "user_2_id"
    t.boolean "is_match"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["user_id"], name: "index_matches_on_user_id"
  end

  create_table "restaurants", force: :cascade do |t|
    t.string "name"
    t.string "description"
    t.string "location"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.bigint "user_id"
    t.bigint "city_id"
    t.boolean "is_approved"
    t.boolean "is_pending"
    t.float "latitude"
    t.float "longitude"
    t.string "avatar"
    t.index ["city_id"], name: "index_restaurants_on_city_id"
    t.index ["user_id"], name: "index_restaurants_on_user_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.string "reset_password_token"
    t.datetime "reset_password_sent_at"
    t.datetime "remember_created_at"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.string "name"
    t.text "description"
    t.date "birthdate"
    t.string "phone_number"
    t.boolean "admin", default: false
    t.bigint "city_id"
    t.string "avatar"
    t.index ["city_id"], name: "index_users_on_city_id"
    t.index ["email"], name: "index_users_on_email", unique: true
    t.index ["reset_password_token"], name: "index_users_on_reset_password_token", unique: true
  end

  add_foreign_key "cita", "restaurants"
  add_foreign_key "cita", "users"
  add_foreign_key "comments", "restaurants"
  add_foreign_key "comments", "users"
  add_foreign_key "matches", "users"
  add_foreign_key "restaurants", "cities"
  add_foreign_key "restaurants", "users"
  add_foreign_key "users", "cities"
end
