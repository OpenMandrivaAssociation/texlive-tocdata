Name:		texlive-tocdata
Version:	55852
Release:	2
Summary:	Adds names to chapters, sections, figures in the TOC and LOF
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tocdata
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocdata.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocdata.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tocdata.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tocdata package may be used to add a small amount of data
to an entry in the table of contents or list of figures,
between the section or caption name and the page number. The
typical use would be to add the name of an author or artist of
a chapter or section, such as in an anthology or a collection
of papers. Additionally, user-level macros are provided which
add the author's name to a chapter or section, along with an
optional prefix and/or suffix, and add to a figure the artist's
name, prefix, and suffix, plus optional additional text. Author
and artist names are also added to the index. Additional
user-level macros control formatting. tocdata works with the
TOC/LOF formatting of the default LaTeX classes, memoir,
koma-script, and with titletoc, tocloft, tocbasic, and
tocstyle.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/tocdata
%{_texmfdistdir}/tex/latex/tocdata
%doc %{_texmfdistdir}/doc/latex/tocdata

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
