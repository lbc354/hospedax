document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('.valor-formatado');

    inputs.forEach(input => {
        input.addEventListener('input', function () {
            let value = input.value;

            // Remove tudo que não for número
            value = value.replace(/\D/g, '');

            if (!value) {
                input.value = '';
                return;
            }

            // Preenche com zeros à esquerda se tiver menos de 3 dígitos
            while (value.length < 3) {
                value = '0' + value;
            }

            // Separa parte inteira e decimal
            let inteiro = value.slice(0, -2);
            let decimal = value.slice(-2);

            // Remove zeros à esquerda da parte inteira, mas mantém 0 se estiver vazio
            inteiro = inteiro.replace(/^0+/, '') || '0';

            // Aplica separador de milhar
            inteiro = inteiro.replace(/\B(?=(\d{3})+(?!\d))/g, '.');

            // Atualiza valor formatado
            input.value = `${inteiro},${decimal}`;
        });
    });
});