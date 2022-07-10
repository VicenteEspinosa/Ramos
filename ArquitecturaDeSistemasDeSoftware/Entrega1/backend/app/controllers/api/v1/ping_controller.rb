class Api::V1::PingController < ApplicationController

    def create
        @ping = Ping.new(ping_params)
        @ping.save
        render json: @ping
    end

    def user_ping
        @user = User.find(params[:user_id])
        @pings = @user.received_pings
        render json: @pings
    end

    private

    def ping_params
        params.require(:ping).permit(:sender_id, :receiver_id)
    end
end
