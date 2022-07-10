json.extract! citum, :id, :user_id, :restaurant_id, :date, :created_at, :updated_at, :is_checked, :is_finished
json.url citum_url(citum, format: :json)
