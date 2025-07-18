:set number
:syntax on
:set nohlsearch
:set smartindent
:set autoindent

autocmd BufRead,BufNewFile *.htm,*.html,*.css,*.js setlocal tabstop=2 shiftwidth=2 softtabstop=2

" plugin manager
call plug#begin()

Plug 'elihunter173/dirbuf.nvim'
Plug 'folke/tokyonight.nvim'

call plug#end()

colorscheme tokyonight
