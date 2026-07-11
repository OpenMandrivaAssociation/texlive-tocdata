%global tl_name tocdata
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.07
Release:	%{tl_revision}.1
Summary:	Adds names to chapters, sections, figures in the TOC and LOF
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tocdata
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tocdata.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tocdata.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tocdata.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The tocdata package may be used to add a small amount of data to an
entry in the table of contents or list of figures, between the section
or caption name and the page number. The typical use would be to add the
name of an author or artist of a chapter or section, such as in an
anthology or a collection of papers. Additionally, user-level macros are
provided which add the author's name to a chapter or section, along with
an optional prefix and/or suffix, and add to a figure the artist's name,
prefix, and suffix, plus optional additional text. Author and artist
names are also added to the index. Additional user-level macros control
formatting. tocdata works with the TOC/LOF formatting of the default
LaTeX classes, memoir, koma-script, and with titletoc, tocloft,
tocbasic, and tocstyle.

