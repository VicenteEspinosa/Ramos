json.extract! restaurant, :id, :name, :description, :location, :created_at, :updated_at, :is_approved, :is_pending
json.url restaurant_url(restaurant, format: :json)
