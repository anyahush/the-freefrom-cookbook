 $(document).ready(function(){
    $('.sidenav').sidenav();
    $('select').formSelect();
  });

// Add list item to ingredients list when '+' button hit
// Used from https://github.com/RussOakham/wanderlust-recipes/blob/master/static/js/script.js
$('#ingredients .add-ingredient-list-item').click(function (event) {
  let IngredientItem = `<li class="collection-item">
                              <div class="input-field">
                                  <input name="ingredients" type="text" maxlength="100" pattern="^[A-Za-z0-9 ]*[A-Za-z0-9][A-Za-z0-9 ]*$" required>
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