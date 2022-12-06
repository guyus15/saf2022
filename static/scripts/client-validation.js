const interests = document.querySelectorAll(".interest-select")
const submit_btn = document.querySelector("#submit-btn")

const minimum_number_checked = 3

// Ensures that a minimum number of interests have been selected. 
function validate_checked_interests()
{
    console.log("validating")
    checked_counter = 0

    interests.forEach(x => 
    {
        if (x.checked)
        {
            checked_counter++
        }
    })

    return checked_counter > minimum_number_checked
}

submit_btn.addEventListener("click", validate_checked_interests);