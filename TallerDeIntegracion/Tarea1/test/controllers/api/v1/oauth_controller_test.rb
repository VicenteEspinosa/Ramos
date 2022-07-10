require "test_helper"

class Api::V1::OauthControllerTest < ActionDispatch::IntegrationTest
  test "should get request" do
    get api_v1_oauth_request_url
    assert_response :success
  end

  test "should get grant" do
    get api_v1_oauth_grant_url
    assert_response :success
  end
end
