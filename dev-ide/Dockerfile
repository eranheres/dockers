## Dockerfile for:
## 1. ubuntu
## 2. Zsh & Zsh + Oh My Zsh + Powerlevel10k
## 3. NeoVim

## Build with: docker build -t dev-ide .
## (Note on build - if using MacOS with M1, on host set: export DOCKER_DEFAULT_PLATFORM=linux/amd64)


## Run with 

FROM ubuntu

RUN apt-get update && apt-get install -y curl git vim wget zsh make pip npm cargo 

# Set the default shell to zsh
RUN chsh -s $(which zsh) $(whoami)
# Install oh-my-zsh: https://ohmyz.sh
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
# Install Powerlevel10k: https://github.com/romkatv/powerlevel10k
RUN git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
RUN echo 'ZSH_THEME="powerlevel10k/powerlevel10k"' >> ~/.zshrc

# NeoVim
RUN curl -LO https://github.com/neovim/neovim/releases/latest/download/nvim-linux64.tar.gz
RUN rm -rf /opt/nvim
RUN tar -C /opt -xzf nvim-linux64.tar.gz
RUN echo 'export PATH="$PATH:/opt/nvim-linux64/bin"' >> ~/.zshrc

# Lazyvim
RUN git clone https://github.com/LazyVim/starter ~/.config/nvim
RUN /opt/nvim-linux64/bin/nvim --headless -c 'Lazy install' +q



