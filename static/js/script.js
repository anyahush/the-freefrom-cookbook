 /*jshint esversion: 8 */
 $(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.collapsible').collapsible();
    $('.tabs').tabs();
    $('.modal').modal();
    $('.tooltipped').tooltip();

    // Used from Code Institute Task Manager, full details in README
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


// Create and Edit Recipes

// Add allergen to list if selected in drop down
// Modified from Wanderlust Recipes, full details in README
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
  
  // Remove allergen from list if selected
  $('#allergen_list').on("click", ".remove-list-item", function (event) {
    $(this).parent().remove();
  });


// Add ingredient to list when + button is clicked
$('#ingredients .add-ingredient-list-item').click(function (event) {
  let IngredientItem = `<li class="collection-item">
                              <div class="input-field">
                                  <input name="ingredients" type="text" class="validate" title="1-100 characters" pattern="^(?=.*[a-zA-Z0-9_ ]){1,100})$" required>
                                  <label for="ingredients">Add quantity and ingredient</label>
                              </div>
                              <a class="remove-list-item">
                                  <i class="fas fa-times"></i>
                                  <span class="sr-only">Remove ingredient</span>
                              </a>
                          </li>`;
  $(this).parent().before(IngredientItem);
});

// Remove ingredient list item on click
$('#ingredients').on("click", ".remove-list-item", function (event) {
  $(this).parent().remove();
});

// Add Method Step item to method step list when '+' button hit
$('#method_step .add-method-step-item').click(function (event) {
  let methodStep = `<li class="collection-item">
                          <div class="input-field">
                          <textarea name="method_step" class="materialize-textarea" pattern="^(?=.*[a-zA-Z0-9_ ]){1,100})$" required></textarea>
                          <label for="method_step">Step description</label>
                          </div>
                          <a class="remove-list-item">
                          <i class="fas fa-times"></i>
                          <span class="sr-only">Remove method step</span>
                      </a>
                      </li>`;
  $(this).parent().before(methodStep);
});

// Remove Method step item on click
$('#method_step').on("click", ".remove-list-item", function (event) {
  $(this).parent().remove();
});
// End of Wanderlust code 


// Checkbox toggle to select all checkboxes in create and
// remove shopping list items
// Used from Stack Overflow, full details in README
$('#select-all').click(function(event) {   
  if(this.checked) {
      // Iterate each checkbox
      $(':checkbox').each(function() {
          this.checked = true;                        
      });
  } else {
      $(':checkbox').each(function() {
          this.checked = false;                       
      });
  }
}); 