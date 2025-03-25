from diffusers import AutoPipelineForText2Image
import torch

# Remove torch_dtype para evitar erro de dtype na CPU
pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo") 
pipe.to("cpu")
#se for utilizar o codigo em outro codigo, voce deve copiar as duas linhas a cima


def criar_imagem(pipe,  prompt):
    image = pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]

    image.show()  # Para visualizar a imagem
    image.save("output.png")  # Para salvar a imagem

def main():
    while True: #looping de interação
    
        user_input = input("desenhe a sua imaginação: ") #pede o input do usuário para utilizar como prompt para a geração de imagem

        if user_input.lower() == "sair":
            print("obrigada e volte sempre")
            break

        else:

            prompt = user_input
            criar_imagem(pipe, prompt) #chama a função para criar a imagem com o prompt do usuário
            print(f'aqui esta a sua imagem com o seu prompt: "{prompt}"')

if __name__ == "__main__":
    main()

#eu fiz isso sem usar o chat gpt!
