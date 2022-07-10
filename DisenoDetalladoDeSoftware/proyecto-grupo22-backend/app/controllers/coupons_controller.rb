class CouponsController < ApplicationController
  before_action :set_coupon, only: %i[ show edit update destroy ]

  # GET /coupons/new
  def new
    @coupon = Coupon.new
  end

  # GET /coupons or /coupons.json
  def index
    @coupons = Coupon.all
  end

  # GET /coupons/1 or /coupons/1.json
  def show
  end

  # GET /coupons/1/edit
  def edit
  end

  # POST /coupons or /coupons.json
  def create
    @coupon = Coupon.new(coupon_params)

    respond_to do |format|
      if @coupon.save
        format.html { redirect_to coupon_url(@coupon), notice: "Coupon was successfully created." }
        format.json { render :show, status: :created, location: @coupon }
      else
        format.html { render :new, status: :unprocessable_entity }
        format.json { render json: @coupon.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /coupons/1 or /coupons/1.json
  def update
    respond_to do |format|
      if @coupon.update(coupon_params)
        format.html { redirect_to coupon_url(@coupon), notice: "Coupon was successfully updated." }
        format.json { render :show, status: :ok, location: @coupon }
      else
        format.html { render :edit, status: :unprocessable_entity }
        format.json { render json: @coupon.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /coupons/1 or /coupons/1.json
  def destroy
    @coupon.destroy

    respond_to do |format|
      format.html { redirect_to coupons_url, notice: "Coupon was successfully destroyed." }
      format.json { head :no_content }
    end
  end

  def verify
    coupon = Coupon.find_by(name: params[:code])
    if coupon
      render json: {coupon_id: coupon.id, value: coupon.value}, status: 200
    else
      render json: {data: "Cupón inválido"}, status: 400
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_coupon
      @coupon = Coupon.find(params[:id])
    end

    # Only allow a list of trusted parameters through.
    def coupon_params
      params.require(:coupon).permit(:name, :value, :category_id)
    end
end
