 $(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.collapsible').collapsible();
    $('.tabs').tabs();
    $('.modal').modal();

    // used from Code Institute Task Manager full details in README
    validateMaterializeSelect();
    function validateMaterializeSelect() {
      let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
      let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
      if ($("select.validate").prop("required")) {
          $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
    }
    $(".select-wrapper input.select-dropdown").on("focusin", function () {
        $(this).parent(".select-wrapper").on("change", function () {
            if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                $(this).children("input").css(classValid);
            }
        });
    }).on("click", function () {
        if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
            $(this).parent(".select-wrapper").children("input").css(classValid);
        } else {
            $(".select-wrapper input.select-dropdown").on("focusout", function () {
                if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                    if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                        $(this).parent(".select-wrapper").children("input").css(classInvalid);
                    }
                }
            });
        }
    });
  }
});
//End of CI code



// Add list item to ingredients list when '+' button hit
// Modified from https://github.com/RussOakham/wanderlust-recipes/blob/master/static/js/script.js
$('#allergen_list .add-allergern-list-item').click(function (event) {
    let AllergenItem = `<select multiple id="allergen_list" name="allergen_list" class="validate" required>
                            <option value="" disabled selected>Select</option>
                                {% for allergen in allergens %}
                                    <option value="{{ allergen.allergen_name }}">{{ allergen.allergen_name }}</option>
                                {% endfor %}
                        </select>
                        <label for="allergen_list">Free From</label>`;
    $(this).parent().before(AllergenItem);
});
  
  // Remove ingredient list item on click
  $('#allergen_list').on("click", ".remove-list-item", function (event) {
    $(this).parent().remove();
  });

$('#ingredients .add-ingredient-list-item').click(function (event) {
  let IngredientItem = `<li class="collection-item">
                              <div class="input-field">
                                  <input name="ingredients" type="text" class="validate" title="1-100 characters" pattern="^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{,100})$" required>
                                  <label for="ingredients">Ingredient</label>
                              </div>
                              <a class="remove-list-item">
                                  <i class="fas fa-times"></i>
                                  <span class="sr-only">Remove Ingredient</span>
                              </a>
                          </li>`;
  $(this).parent().before(IngredientItem);
});

// Remove ingredient list item on click
$('#ingredients').on("click", ".remove-list-item", function (event) {
  $(this).parent().remove();
});

// Add Method Step item to ingredients list when '+' button hit
$('#method_step .add-method-step-item').click(function (event) {
  let methodStep = `<li class="collection-item">
                          <a class="remove-list-item">
                              <i class="fas fa-times"></i>
                              <span class="sr-only">Remove Method Step</span>
                          </a>
                          <div class="input-field">
                          <textarea name="method_step" class="materialize-textarea" required></textarea>
                          <label for="method_step">Step Description</label>
                          </div>
                      </li>`;
  $(this).parent().before(methodStep);
});

// Remove Method step item on click
$('#method_step').on("click", ".remove-list-item", function (event) {
  $(this).parent().remove();
});
// End of Wanderlust code 
