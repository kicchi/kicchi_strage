set number
set autoindent
set hlsearch
syntax on
colorscheme darkblue
set tabstop=4
set noswapfile


" map

inoremap {- {<cr>}<esc>ko<tab>
inoremap st- std::
inoremap fi- first
inoremap sc- second

inoremap tmp- <esc>:r ~/aoj/main.cpp<cr>kdd
inoremap make- <esc>:r ~/aoj/Makefile<cr>

inoremap pv- void printv(vi v){<cr><tab>for(int i = 0; i < v.size(); i++){<cr><tab>cout << v[i] << " ";<cr>}cout << endl;<cr>return ;<cr>}

cnoremap v- tabe ~/.vimrc
cnoremap r- source ~/.vimrc

imap dbg- std::cout << "debug " << std::endl;<esc>F"i

" for
inoremap fo- for () {<cr>}<esc>kf(a
inoremap for- <esc>^"cywf,l"vywccfor () {<cr>}<esc>kf(aint <c-r>c = 0; <c-r>c < <c-r>v; <c-r>c++<esc>o
inoremap rep- <esc>^"cywf,l"vywf,l"bywccfor () {<cr>}<esc>kf(aint <c-r>c = <c-r>v; <c-r>c < <c-r>b; <c-r>c++<esc>o


" cin
inoremap cin1 <esc>^w"cywf;a cin >> <c-r>c;
inoremap cin2 <esc>^w"cywf,l"vywf;a cin >> <c-r>c >> <c-r>v;
inoremap cin3 <esc>^w"cywf,l"vywf,l"bywf;a cin >> <c-r>c >> <c-r>v >> <c-r>b;
" cout
inoremap co- cout <<  << endl;<esc>3F a
" vector
inoremap vi- vector<int> 
inoremap pb- push_back();<esc>hi
inoremap vii- vector<vector<int>>
inoremap vd- vector<double>
inoremap vs- vector<string>
inoremap vpii- vector<pair<int,int>>

noremap <S-h> ^
noremap <S-l> $

noremap <tab>n gt

inoremap re- return 


"vector


