require "application_system_test_case"

class GustosTest < ApplicationSystemTestCase
  setup do
    @gusto = gustos(:one)
  end

  test "visiting the index" do
    visit gustos_url
    assert_selector "h1", text: "Gustos"
  end

  test "creating a Gusto" do
    visit gustos_url
    click_on "New Gusto"

    fill_in "Descripcion", with: @gusto.descripcion
    fill_in "Nombre", with: @gusto.nombre
    click_on "Create Gusto"

    assert_text "Gusto was successfully created"
    click_on "Back"
  end

  test "updating a Gusto" do
    visit gustos_url
    click_on "Edit", match: :first

    fill_in "Descripcion", with: @gusto.descripcion
    fill_in "Nombre", with: @gusto.nombre
    click_on "Update Gusto"

    assert_text "Gusto was successfully updated"
    click_on "Back"
  end

  test "destroying a Gusto" do
    visit gustos_url
    page.accept_confirm do
      click_on "Destroy", match: :first
    end

    assert_text "Gusto was successfully destroyed"
  end
end
