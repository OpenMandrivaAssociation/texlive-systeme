# revision 23336
# category Package
# catalog-ctan /macros/generic/systeme
# catalog-date 2011-06-24 11:48:53 +0200
# catalog-license lppl1.3
# catalog-version 0.2b
Name:		texlive-systeme
Version:	0.2b
Release:	1
Summary:	Format systems of equations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/systeme
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/systeme.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/systeme.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows you to enter systems of equations or
inequalities in an intuitive way, and produces typeset output
where the terms and signs are aligned vertically. The package
works with plain TeX or LaTeX, but e-TeX is required. Cette
petite extension permet de saisir des systemes d'equations ou
inequations de facon intuitive, et produit un affichage ou les
termes et les signes sont alignes verticalement.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/systeme/systeme.sty
%{_texmfdistdir}/tex/generic/systeme/systeme.tex
%doc %{_texmfdistdir}/doc/generic/systeme/README
%doc %{_texmfdistdir}/doc/generic/systeme/systeme_doc_fr.pdf
%doc %{_texmfdistdir}/doc/generic/systeme/systeme_doc_fr.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
