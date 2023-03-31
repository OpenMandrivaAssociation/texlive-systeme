Name:		texlive-systeme
Version:	55015
Release:	2
Summary:	Format systems of equations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/systeme
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/systeme.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/systeme.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows you to enter systems of equations or
inequalities in an intuitive way, and produces typeset output
where the terms and signs are aligned vertically. The package
works with plain TeX or LaTeX, but e-TeX is required. Cette
petite extension permet de saisir des systemes d'equations ou
inequations de facon intuitive, et produit un affichage ou les
termes et les signes sont alignes verticalement.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/systeme
%doc %{_texmfdistdir}/doc/generic/systeme

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
