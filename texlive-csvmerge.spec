%global tl_name csvmerge
%global tl_revision 51857

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Merge TeX code with csv data
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/csvmerge
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csvmerge.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csvmerge.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/csvmerge.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros for processing a csv spreadsheet file with
a minimum of configuration for the csv file. The first row names the
columns and the remaining rows are data. This data can be merged with
TeX code residing in an auxiliary file and the process repeated for each
data row. There is one macro to set things up, one to extract the data,
and one to tell if the field is empty or not. The documentation contains
examples.

