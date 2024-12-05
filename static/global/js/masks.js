document.addEventListener("DOMContentLoaded", function () {
    const cpfInput = document.querySelector("#cpf");
    const phoneInput = document.querySelector("#phone");
    
    function CPFMask(input) {
        input.addEventListener("input", function () {
            let value = input.value.replace(/\D/g, ''); 
            value = value.replace(/(\d{3})(\d)/, '$1.$2');
            value = value.replace(/(\d{3})(\d)/, '$1.$2'); 
            value = value.replace(/(\d{3})(\d{1,2})$/, '$1-$2'); 
            input.value = value;
        });
    }

    function PhoneMask(input) {
        input.addEventListener("input", function () {
            let value = input.value.replace(/\D/g, ''); 
            value = value.replace(/(\d{2})(\d)/, '($1) $2'); 
            value = value.replace(/(\d{5})(\d)/, '$1-$2'); 
            input.value = value;
        });
    }

    if (cpfInput) CPFMask(cpfInput);
    if (phoneInput) PhoneMask(phoneInput);
});
