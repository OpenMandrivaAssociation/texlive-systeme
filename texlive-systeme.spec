%global tl_name systeme
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.51
Release:	%{tl_revision}.1
Summary:	Format systems of equations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/systeme
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/systeme.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/systeme.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows you to enter systems of equations or inequalities in
an intuitive way, and produces typeset output where the terms and signs
are aligned vertically. The package works with plain TeX or LaTeX, but
e-TeX is required. Cette petite extension permet de saisir des systemes
d'equations ou inequations de facon intuitive, et produit un affichage
ou les termes et les signes sont alignes verticalement.

