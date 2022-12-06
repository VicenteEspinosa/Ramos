json.extract! product, :id, :price, :category, :amount, :name, :created_at, :updated_at
json.url product_url(product, format: :json)
