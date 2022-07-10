require 'test_helper'

class GustosControllerTest < ActionDispatch::IntegrationTest
  setup do
    @gusto = gustos(:one)
  end

  test "should get index" do
    get gustos_url
    assert_response :success
  end

  test "should get new" do
    get new_gusto_url
    assert_response :success
  end

  test "should create gusto" do
    assert_difference('Gusto.count') do
      post gustos_url, params: { gusto: { descripcion: @gusto.descripcion, nombre: @gusto.nombre } }
    end

    assert_redirected_to gusto_url(Gusto.last)
  end

  test "should show gusto" do
    get gusto_url(@gusto)
    assert_response :success
  end

  test "should get edit" do
    get edit_gusto_url(@gusto)
    assert_response :success
  end

  test "should update gusto" do
    patch gusto_url(@gusto), params: { gusto: { descripcion: @gusto.descripcion, nombre: @gusto.nombre } }
    assert_redirected_to gusto_url(@gusto)
  end

  test "should destroy gusto" do
    assert_difference('Gusto.count', -1) do
      delete gusto_url(@gusto)
    end

    assert_redirected_to gustos_url
  end
end
