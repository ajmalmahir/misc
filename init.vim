" number in margin
:set number
" syntax highlighting
:syntax on
" use spaces to insert a <TAB>
:set expandtab
" <TAB> indents with 4 space width
:set tabstop=4
" when indenting with '>', use 4 space width
:set shiftwidth=4

" plugin manager
call plug#begin()

Plug 'preservim/nerdtree'

call plug#end()
