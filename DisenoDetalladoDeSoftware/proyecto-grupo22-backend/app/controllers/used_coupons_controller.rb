class UsedCouponsController < ApplicationController
  def index
    render json: UsedCouponSerializer.new(
      UsedCoupon.all,
      { is_collection: true }
    ).serializable_hash, status: 200
  end
end
