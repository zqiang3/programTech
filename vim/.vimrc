set nu
"set cindent
set autoindent

set tabstop=4
set expandtab
set shiftwidth=4
set softtabstop=4

set noswapfile

""inoremap { {<CR>}<Esc>ka<CR><tab>
inoremap { {<CR>}<Esc>kA<CR><tab>
"inoremap { {<CR>}<Up><End><CR><tab>
""inoremap { {}<left>
inoremap ( ()<left>
inoremap " ""<left>
inoremap ' ''<left>
inoremap [ []<left>

map <F3> i"<Esc>xea"<Esc>x
imap <C-r> <right>
imap <C-e> <END>
imap <C-a> <HOME>


"colorscheme molokai

let g:neocomplcache_enable_at_startup = 1
let g:neocomplcache_enable_smart_case = 1
let g:neocomplcache_enable_auto_select = 1

" C的编译和运行
map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
exec "w"
exec "!gcc % -g -o %<"
exec "!time ./%<"
endfunc

map <F9> :call CompileRunGccp()<CR>
func! CompileRunGccp()
exec "w"
exec "!g++ % -g -o %<"
exec "!time ./%<"
endfunc

" Python脚本运行"
map <F8> :call RunPython()<CR>
func! RunPython()
exec "w"
exec "!python %"
endfunc
