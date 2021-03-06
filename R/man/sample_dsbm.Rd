% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/sampling.R
\name{sample_dsbm}
\alias{sample_dsbm}
\title{Sample a directed stochastic block model (DSBM)}
\usage{
sample_dsbm(
  block_sizes,
  connection_matrix,
  weight_matrix = NULL,
  sample_weight_type = c("unweighted", "constant", "poisson")
)
}
\arguments{
\item{block_sizes}{A vector containing the size of each block of vertices.}

\item{connection_matrix}{A matrix containing the block-to-block connection
probabilities.}

\item{weight_matrix}{A matrix containing the block-to-block weight
parameters.
Unused for \code{sample_weight_type = "constant"}.
Defaults to \code{NULL}.}

\item{sample_weight_type}{The type of weighting scheme.
One of \code{"unweighted"}, \code{"constant"} or \code{"poisson"}.}
}
\value{
A randomly sampled (weighted) adjacency matrix of a DSBM.
}
\description{
Sample the (weighted) adjacency matrix of a (weighted) directed stochastic
block model (DSBM) with specified parameters.
}
\examples{
block_sizes <- c(10, 10)
connection_matrix <- matrix(c(0.8, 0.1, 0.1, 0.8), nrow = 2, byrow = TRUE)
weight_matrix <- matrix(c(10, 3, 3, 10), nrow = 2, byrow = TRUE)
sample_dsbm(block_sizes, connection_matrix, weight_matrix, "poisson")
}
