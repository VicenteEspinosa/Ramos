class UserMailer < ApplicationMailer
    def new_user_email
        @user = params[:user]
        @token = params[:token]
        mail(to: @user.mail, subject: 'Confirmar Correo')
    end
end
