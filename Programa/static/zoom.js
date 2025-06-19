// Espera o DOM carregar para garantir que os elementos existam
document.addEventListener("DOMContentLoaded", () => {
  // Seleciona todas as imagens com a classe "zoom-img"
  const imgs = document.querySelectorAll(".zoom-img");

  // Para cada imagem encontrada, adiciona os eventos necessários
  imgs.forEach(img => {
    let zoomed = false; // Controle do estado do zoom (ativado ou não)
    // Define uma transição suave para o transform (zoom)
    img.style.transition = "transform 0.3s ease";

    // Evento de clique na imagem para ativar/desativar o zoom
    img.addEventListener("click", () => {
      zoomed = !zoomed; // Alterna o estado do zoom
      // Aplica o zoom (scale 2) se zoom estiver ativo, senão volta ao normal (scale 1)
      img.style.transform = zoomed ? "scale(2)" : "scale(1)";
      // Se o zoom foi desativado, reseta o ponto de origem do zoom para o centro
      if (!zoomed) {
        img.style.transformOrigin = "center center";
      }
    });

    // Evento que acompanha o movimento do mouse na imagem
    img.addEventListener("mousemove", (e) => {
      // Se o zoom não estiver ativado, não faz nada
      if (!zoomed) return;

      // Obtém o retângulo da imagem (posição e tamanho)
      const rect = img.getBoundingClientRect();
      // Calcula a posição percentual do mouse dentro da imagem (horizontal)
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      // Calcula a posição percentual do mouse dentro da imagem (vertical)
      const y = ((e.clientY - rect.top) / rect.height) * 100;

      // Define o ponto de origem da transformação para o local do mouse
      img.style.transformOrigin = `${x}% ${y}%`;
    });
  });
});