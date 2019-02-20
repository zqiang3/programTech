

```
"colorscheme molokai

"自动补全插件
let g:neocomplcache_enable_at_startup = 1
let g:neocomplcache_enable_smart_case = 1
let g:neocomplcache_enable_auto_select = 1

"tab键转为空格
set tabstop=4                   "设置tab键宽度
set softtabstop=4
set shiftwidth=4                "自动缩进使用的空白长度
set expandtab                   "将tab转换为空格

set nu                          "设置行号
set autoindent                  "自动缩进 take indent for new linefrom 
set cindent                     "针对c语言自动缩进
previous line
set noswapfile                  "禁止生成临时文件
set noundofile                  "automatically saves undo history to an undo file
set nowrapscan
set showmatch
"set mouse=a                     "可以在buffer的任何地方使用鼠标

"行首 行尾
imap <C-e> <END>
imap <C-a> <HOME>

"选中全部
map <C-a> ggVG

"删除
imap <C-u> <esc>d0i
imap <C-k> <esc>d$
inmap <C-d> dd
imap <C-d> <esc>ddi
map <C-d> dd

"补全
"inoremap { {<CR>}<Esc>ka<CR><tab>          "若c语言自动缩进，可删去最后的<tab>
"inoremap { {}<Esc>i<CR><Up><Right><CR><tab>
inoremap { {}<left>
inoremap [ []<left>
inoremap ( ()<left>
inoremap < <><left>
inoremap " ""<left>
inoremap ' ''<left>

"一键运行 c, c++, python
map <F5> :call CompileRunGcc()<CR>
func! CompileRunGcc()
    exec "w"
    if &filetype == 'c'
        exec '!g++ % -o %<'
        exec '!time ./%<'
    elseif &filetype == 'c'
        exec '!g++ % -o %<'
        exec '!time ./%<'
    elseif &filetype == 'python'：x
        exec '!time python %'

    endif
endfunc

"保存
func! SaveFile()
    exec "w"
endfunc

map <leader>s :call SaveFile()<CR>
imap <leader>s <ESC>:call SaveFile()<CR>
vmap <leader>s <ESC>:call SaveFile()<CR>

```

