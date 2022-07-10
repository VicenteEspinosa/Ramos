json.extract! coupon, :id, :name, :value, :category_id, :created_at, :updated_at
json.url coupon_url(coupon, format: :json)
